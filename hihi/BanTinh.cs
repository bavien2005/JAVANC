using UnityEngine;

public class BanTinh : MonoBehaviour
{
    [SerializeField] private float speed;
    private Vector3 dir;
    void Start()
    {
        Destroy(gameObject, 3f);
    }

    void Update()
    {
        if (dir == Vector3.zero)
        {
            return;
        }
        transform.position += dir * speed * Time.deltaTime;
    }

    public void SetDir(Vector3 dir)
    {
        this.dir = dir.normalized;
    }
}
